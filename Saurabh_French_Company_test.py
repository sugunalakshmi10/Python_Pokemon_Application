'''This is used to generate the specific pokeman details
    using :arg(name),
    :return list
'''
import sys
import csv
import requests

def describe_pokemon(pokemon_name):
    '''This function :func used to generate pokemon row
       :arg(names) is a list of pokemon names
       :return is returning the corresponding pokemon row
    '''
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/%s/"%pokemon_name
    response = requests.get(url_pokemon)
    final = []
    if response.status_code == 200:
        data = response.json()
        arr = []
        t = data['types']
        if len(t) > 1:
            for i, _ in enumerate(data['types']):
                arr.append(t[i]['type']['name'])
                d = "|".join(arr)
        else:
            d = t[0]['type']['name']
        final.extend([data['id'], data['name'], data['weight'], d])
    return final


if __name__ == '__main__':
    with open("csv_out.csv", "w", newline="") as output_file:
        output = csv.writer(output_file)
        output.writerow(['ID', 'NAME', 'WEIGHT', 'TYPES'])
        names = list(sys.argv)[1:]
        if len(names) != 0:
            for name in names:
                res = describe_pokemon(name.lower())
                if res != list():
                    output.writerow(res)
                    print(",".join(map(str, res)))
                else:
                    print("{} doesnot Exist".format(name))
        else:
            print("Please Enter Pokemon name")
