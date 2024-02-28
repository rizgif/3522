"""
This module depicts the use of asyncio and aiohttp to make HTTP GET
requests.
"""
import aiohttp
import asyncio
import platform


async def get_starwars_people_data(id_: int, url: str, session: aiohttp.ClientSession) -> dict:
    """
    An async coroutine that executes GET http request. The response is
    converted to a json. The HTTP request and the json conversion are
    asynchronous processes that need to be awaited.
    :param id_: an int
    :param url: a string, the unformatted url (missing parameters)
    :param session: a HTTP session
    :return: a dict, json representation of response.
    """

    target_url = url.format(id_)
    response = await session.request(method="GET", url=target_url)
    print("Response object from aiohttp:\n", response)
    print("Response object type:\n", type(response))
    print("-----")
    json_dict = await response.json()
    return json_dict


async def process_single_request(id_) -> dict:
    """
    This function depicts the use of await to showcase how one async
    coroutine can await another async coroutine
    :param id_: an int
    :return: dict, json response
    """
    url = "https://swapi.dev/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_single_request")
        response = await get_starwars_people_data(id_, url, session)
        print(response)
        return response


async def process_requests(requests: list) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async coroutines concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """
    url = "https://swapi.dev/api/people/{}/"
    async with aiohttp.ClientSession() as session:
        print("***process_requests")
        async_coroutines = [get_starwars_people_data(id_, url, session) for id_ in requests]

        responses = await asyncio.gather(*async_coroutines)

        for response in responses:
            print(response)
        return responses


async def main():

    #get a single star wars character's data
    response = await process_single_request(1) #get Luke's data using async coroutine

    #get multiple star wars characters' data at once
    requests = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    responses = await process_requests(requests) #get characters' data using async coroutine

if __name__ == '__main__':
    asyncio.run(main())