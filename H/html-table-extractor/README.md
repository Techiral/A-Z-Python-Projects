# To run this:
- `pip3 install -r requirements.txt`
- To extract all tables from this [wikipedia page](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population):
    ```
    python html_table_extractor.py https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
    ```
    This will download all HTML tables and save them as CSV files in your current directory.