import requests


def validate_reponse(func):
    def wrapper(*args,**kwargs):
        response = func(*args,**kwargs)
        if response.status_code == 200:
            lst_response = response.json()
            if len(lst_response)>1:
                return lst_response
        else:
            return None
    return wrapper

@validate_reponse
def get_response(cnt_code):
    payload = {"format": "json"}
    cnt = cnt_code
    response = requests.get(
        f"https://api.worldbank.org/v2/country/{cnt}",
        params=payload
    )
    return response

def ingestion(lst_response,dict_db):
    dict_response = lst_response[1][0]
    name = dict_response["name"]
    dict_db[name] = dict()
    dict_db[name]["id"] = dict_response["id"]
    dict_db[name]["capital"] = dict_response["capitalCity"]
    print(f"Ingested {name} details")
    return dict_db

def search_details(dict_db,cnt_name):
    return dict_db.get(cnt_name.title(),"Details not found")


def main():
    dict_db = {}
    while True:
        try:
            option = int(input("Enter the option \n 1: Search\n 2: Ingest \n 3: Exit \n"))
            if option == 1:
                cnt_name = input("Enter Country name\n")
                print(search_details(dict_db=dict_db,cnt_name=cnt_name))
            if option == 2:
                cnt_code = input("Enter a country code\n")
                response = get_response(cnt_code=cnt_code.lower())
                if response is not None:
                    ingestion(lst_response=response,dict_db=dict_db)
                else:
                    print("Enter valid Country code")
            if option == 3:
                print("Good Bye")
                break
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("Good Bye")
            break



if __name__ == "__main__":
    main()
