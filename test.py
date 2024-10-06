
def reverse_word(word):
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

def is_palindrome(word):
        return word == reverse_word(word)

def check_all_palindromes(arr):
        for word in arr:
                if is_palindrome(word) == False:
                        return False
        return True



print(check_all_palindromes(['racecar','bab','pap']))



frequency_map = {}
n=100100000
while n > 0:
    
    digit = n % 10
    if digit not in frequency_map:
            frequency_map[digit] = 1
    else:
            frequency_map[digit]+=1
    n = int(n//10)

print(frequency_map)




def create_staircase(nums):
  while len(nums) != 0:
    print('here')
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets
       

print(create_staircase([1, 2, 3, 4, 5, 6, 7]))
print(create_staircase([1, 2, 3, 4, 5, 6]))

# import pandas as pd
# # sheetId = '1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo' ## REPLACE WITH YOUR SHEETID
# sheetUrl = f'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
# sheetDF = pd.read_html(sheetUrl, skiprows=1)[0]

# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

# # print("here", sheetDF[0][1], "there", sheetDF[2][1])
# print(type(sheetDF))
# # print(sheetDF[0][2], sheetDF[2][2])

# data = sheetDF

# def create_and_print_grid(data):
#     for row in data:
#          for col in data:
#               print(data[row][col])
              
#     # Initialize grid dimensions
#     max_x = max(entry['x-coordinate'] for entry in data)
#     max_y = max(entry['y-coordinate'] for entry in data)

#     # Create a grid filled with spaces
#     grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

#     # Place characters in the grid
#     for entry in data:
#         character = entry['Character']
#         x = entry['x-coordinate']
#         y = entry['y-coordinate']
#         grid[y][x] = character

#     # Print the grid
#     for row in grid:
#         print(''.join(row))


# create_and_print_grid(data)


# import pandas as pd

# def retrieve_data_from_doc(url):
#     # Read the HTML table from the Google Doc URL
#     try:
#         # Read the first table in the HTML
#         sheetDF = pd.read_html(url)[0]
#     except Exception as e:
#         print(f"Error reading the document: {e}")
#         return None

#     return sheetDF

# def inspect_dataframe(df):
#     # Print the columns and the first few rows of the DataFrame
#     print("Columns:", df.columns)
#     print("First few rows of the DataFrame:")
#     print(df.head())

# def parse_data(df):
#     grid_info = []
#     max_x, max_y = 0, 0

#     # Rename columns based on the actual header row
#     df.columns = df.iloc[0]
#     df = df[1:]
#     df.reset_index(drop=True, inplace=True)
    
#     # Iterate over the DataFrame to extract data
#     for _, row in df.iterrows():
#         try:
#             character = row['Character']
#             x = int(row['x-coordinate'])
#             y = int(row['y-coordinate'])
            
#             # Track the maximum x and y values for grid size
#             max_x = max(max_x, x)
#             max_y = max(max_y, y)

#             grid_info.append((character, x, y))
#         except KeyError as e:
#             print(f"Missing expected column: {e}")
#         except ValueError as e:
#             print(f"Error converting values: {e}")

#     return grid_info, max_x, max_y

# def create_and_print_grid(grid_info, max_x, max_y):
#     # Initialize grid with spaces
#     grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

#     # Fill grid with characters
#     for character, x, y in grid_info:
#         grid[y][x] = character

#     # Print grid
#     for row in grid:
#         print(''.join(row))

# def decode_secret_message(url):
#     # Step 1: Retrieve data from Google Doc
#     df = retrieve_data_from_doc(url)
#     if df is None:
#         return

#     # Step 2: Inspect the DataFrame to check column names
#     inspect_dataframe(df)

#     # Step 3: Parse data
#     grid_info, max_x, max_y = parse_data(df)

#     # Step 4: Create and print the grid
#     create_and_print_grid(grid_info, max_x, max_y)

# # Example usage
# doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
# decode_secret_message(doc_url)

import pandas as pd

def retrieve_data_from_doc(url):
    # Read the HTML table from the Google Doc URL
    try:
        sheetDF = pd.read_html(url)[0]  # Read the first table in the HTML
    except Exception as e:
        print(f"Error reading the document: {e}")
        return None

    return sheetDF

def inspect_dataframe(df):
    # Print the columns and the first few rows of the DataFrame
    print("Columns:", df.columns)
    print("First few rows of the DataFrame:")
    print(df.head())

def parse_data(df):
    grid_info = []
    max_x, max_y = 0, 0

    # Rename columns based on the actual header row
    df.columns = df.iloc[0]
    df = df[1:]
    df.reset_index(drop=True, inplace=True)
    
    # Iterate over the DataFrame to extract data
    for _, row in df.iterrows():
        try:
            character = row['Character']
            x = int(row['x-coordinate'])
            y = int(row['y-coordinate'])
            
            # Track the maximum x and y values for grid size
            max_x = max(max_x, x)
            max_y = max(max_y, y)

            grid_info.append((character, x, y))
        except KeyError as e:
            print(f"Missing expected column: {e}")
        except ValueError as e:
            print(f"Error converting values: {e}")

    return grid_info, max_x, max_y

def create_and_print_grid(grid_info, max_x, max_y):
    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill grid with characters
    for character, x, y in grid_info:
        grid[y][x] = character

    # Reverse the grid to flip it vertically
    grid = grid[::-1]

    # Print grid
    for row in grid:
        print(''.join(row))

def decode_secret_message(url):
    # Step 1: Retrieve data from Google Doc
    df = retrieve_data_from_doc(url)
    if df is None:
        return

    # Step 2: Inspect the DataFrame to check column names
    inspect_dataframe(df)

    # Step 3: Parse data
    grid_info, max_x, max_y = parse_data(df)

    # Step 4: Create and print the grid
    create_and_print_grid(grid_info, max_x, max_y)

# Example usage
doc_url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
decode_secret_message(doc_url)
