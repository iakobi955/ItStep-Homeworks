# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის 
# გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს 
# სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები.
# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ.
# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით.
# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით.

import requests

def get_products():
  try:
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)

    if response.status_code == 200:
      return response.json()
    else:
      return f"Error {response.status_code}: Page not found"
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ERRROR: {http_err}")
  except requests.exceptions.ConnectionError as con_err:
    print(f"CONNECTION ERRROR: {con_err}")
  except Exception as ex:
    print(f"Something wrong: {ex}")


def parse_data():
  products = get_products()

  product_prices = []
  product_categories = set()
  product_titles = []
  product_ratings = []

  for product in products:
    product_prices.append(product['price'])
    product_categories.add(product['category'])
    product_titles.append({'id': product['id'], 'title': product['title']})
    product_ratings.append(product['rating'])

  product_titles.sort(key = lambda x: x['title'])
  product_ratings.sort(key = lambda x: x['rate'])
  


  print("Max price:", max(product_prices), "Min price:", min(product_prices), "Average price:", sum(product_prices) / len(product_prices), "\n")
  print("Product categories:", sorted(product_categories), "\n")
  print("product Titles:", product_titles, "\n")
  print("Product ratings:", product_ratings, "\n")


# =====================
parse_data()
