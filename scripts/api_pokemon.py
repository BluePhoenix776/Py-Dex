import aiohttp
import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class PokeAPIRequester(object):

    async def fetch_data(self, session, url):
        """Realiza una solicitud GET a una URL dada y retorna los datos JSON."""

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                
                else:
                    return {"error": f"{response.status}"}
        
        except Exception as error:
            return {"error": f"{error}"}


    async def fetch_berries(self, item):
        "Obtiene los datos básicos de un Ítem"

        url = f"https://pokeapi.co/api/v2/berry/{item}/"

 

        async with aiohttp.ClientSession() as session:

            berry_data = await self.fetch_data(session, url)
            if "error" in berry_data:
                return berry_data

            # Obtener los datos básicos como Ítem
            item_url = berry_data["item"]["url"]
            item_task = self.fetch_data(session, item_url)
            item_data = await asyncio.gather(item_task)
            item_data =  item_data[0]

            # Obtener los datos de la Bag Pocket
            pocket = await self.fetch_data(session, item_data["category"]["url"])



            return {
                
                "nombre": berry_data["name"],
                "id": berry_data["id"],
                "precio": item_data["cost"],
                "categoria": item_data["category"]["name"],
                "bag_pocket": pocket["pocket"]["name"],
                "descripcion": item_data["flavor_text_entries"][22]["text"]
            }




    async def fetch_items(self, item):
        "Obtiene los datos básicos de un Ítem"

        url = f"https://pokeapi.co/api/v2/item/{item}/"

        try:

            async with aiohttp.ClientSession() as session:

                item_data = await self.fetch_data(session, url)
                if "error" in item_data:
                    return item_data

                # Obtener datos básicos
                pocket_url = item_data["category"]["url"]
                pocket_task = self.fetch_data(session, pocket_url)
                pocket = await asyncio.gather(pocket_task)

                return {
                    
                    "nombre": item_data["name"],
                    "id": item_data["id"],
                    "precio": item_data["cost"],
                    "categoria": item_data["category"]["name"],
                    "bag_pocket": pocket[0]["pocket"]["name"],
                    "descripcion": item_data["flavor_text_entries"][13]["text"]
                }

        except Exception as error:
            return {"error": f"{str(error)}"}
        

    async def fetch_pokemon(self, session, pokemon):
        """Obtiene datos de un Pokémon y realiza peticiones adicionales basadas en URLS relacionadas."""

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

        try:

            pokemon_data = await self.fetch_data(session, url)
            if "error" in pokemon_data:
                return pokemon_data
            
            # Preparar peticiones adicionales

            ## Tipos
            types_urls = [type_["type"]["url"] for type_ in pokemon_data["types"]]
            types_tasks = [self.fetch_data(session, type_url) for type_url in types_urls]
            types = await asyncio.gather(*types_tasks)

            ## Descripción
            specie_url = pokemon_data["species"]["url"]
            specie_task = self.fetch_data(session, specie_url)
            descriptions = await asyncio.gather(specie_task)

            ## Genero
            gender_task = self.fetch_data(session, specie_url)
            gender = await asyncio.gather(gender_task)

            ## Estadisticas Base
            stats_task = self.fetch_data(session, url)
            stats = await asyncio.gather(stats_task)

            stats_dict = {stat["stat"]["name"]: stat["base_stat"] for stat in stats[0]["stats"]}

            ## Habilidades
            
            # Verificamos si el Pokémon tiene habilidad oculta
            hidden_abilities_urls = [
                ability["ability"]["url"] for ability in pokemon_data["abilities"] if ability["is_hidden"]
            ]

            hidden_abilities_tasks = [self.fetch_data(session, hidden_ability_url) for hidden_ability_url in hidden_abilities_urls]
            hidden_abilities = await asyncio.gather(*hidden_abilities_tasks)

            
            abilities_urls = [abilitie["ability"]["url"] for abilitie in pokemon_data["abilities"] if abilitie["is_hidden"] == False]
            ability_tasks = [self.fetch_data(session, ability_url) for ability_url in abilities_urls]
            abilities = await asyncio.gather(*ability_tasks)


            return {

                "nombre": pokemon_data["name"],
                "id": pokemon_data["id"],
                "altura": pokemon_data["height"],
                "peso": pokemon_data["weight"],
                "tipos": [
                    type_url["names"][5]["name"].lower() for type_url in types
                ],
                "habilidades": [
                    ability["names"][5]["name"] for ability in abilities
                ],
                "habilidad oculta": [
                    hidden_ability["names"][5]["name"] for hidden_ability in hidden_abilities
                ],
                "descripción": [
                    (description["flavor_text_entries"][26]["flavor_text"], description["flavor_text_entries"][34]["flavor_text"]) for description in descriptions
                ],
                "genero": gender[0]["gender_rate"],
                "stats": stats_dict
            }
        
        except Exception as error:
            return {"error": f"{str(error)}"}

    async def fetch_all_pokemons(self, pokemon_list):
        """Obtiene información de una lista de Pokémon en paralelo."""

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_pokemon(session, pokemon) for pokemon in pokemon_list]

            return await asyncio.gather(*tasks)


