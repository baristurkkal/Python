import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Load the environment variable

database_url = os.getenv('DATABASE_URL')
# Connect to the PostgreSQL database

def export_orders_to_csv():
    try:
        # Connect to the database
        conn = psycopg2.connect(database_url)
        
        df = pd.read_sql("SELECT * FROM orders", conn)
        df.to_csv("orders.csv", sep='\t',index=False)
        print(f"Exported {len(df)} rows to orders.csv")
        df.order_date.hist().fig
        plt.savefig("orders_histogram.png", dpi=300)ls -ltr

# Close connection
        
        # cursor = conn.cursor()cat 

        # # Execute query
        # cursor.execute("SELECT * FROM orders")
        # rows = cursor.fetchall()

        # Get column names
        # colnames = [desc[0] for desc in cursor.description]

        # # Write to CSV
        # with open("orders.csv", "w", newline="", encoding="utf-8") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(colnames)  # write header
        #     writer.writerows(rows)     # write data

        # print(f"Exported {len(rows)} rows to orders.csv")
        
    except psycopg2.ProgrammingError as ce:
        print("Connection error", ": Invalid URL ",ce)
    except Exception as e:
        print("Error:",type(e), e)
    finally:
        conn.close()
        print("Conenction closed")

if __name__ == "__main__":
    export_orders_to_csv()
