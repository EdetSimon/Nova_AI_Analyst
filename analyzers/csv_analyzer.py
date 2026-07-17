import pandas as pd

class CSVAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    def get_summary(self):
        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
            "column_names": list(self.df.columns),
            "missing": self.df.isnull().sum().to_dict(),
            "data_types": self.df.dtypes.astype(str).to_dict(),
            "numeric_columns": list(self.df.select_dtypes(include="number").columns)
        }

    def generate_statistics(self):
        self.load_data()

        stats = f"""
    Rows: {self.df.shape[0]}
    Columns: {self.df.shape[1]}

    Column Names:
    {', '.join(self.df.columns)}

    Missing Values:
    {self.df.isnull().sum().to_string()}

    Summary Statistics:

    {self.df.describe(include='all').to_string()}
    """

        return stats

    def get_kpis(self):

        kpis = {}

        kpis["total_rows"] = len(self.df)
        kpis["total_columns"] = len(self.df.columns)
        kpis["missing_values"] = int(self.df.isnull().sum().sum())

        revenue_col = self.find_column([
            "Revenue",
            "Total Revenue",
            "Sales",
            "Sales Amount",
            "Amount",
            "Income"
        ])

        if revenue_col:
            kpis["revenue_column"] = revenue_col
            kpis["total_revenue"] = self.df[revenue_col].sum()
            kpis["average_revenue"] = self.df[revenue_col].mean()

        product_col = self.find_column([
            "Product",
            "Product Name",
            "Item",
            "Item Type",
            "Category",
            "Service"
        ])

        if product_col:
            kpis["top_product"] = self.df[product_col].mode().iloc[0]
            kpis["product_column"] = product_col

        region_col = self.find_column([
            "Region",
            "Country",
            "State",
            "City",
            "Location",
            "Area"
        ])

        if region_col:
            kpis["top_region"] = self.df[region_col].mode().iloc[0]
            kpis["region_column"] = region_col

        return kpis

        return kpis

    def find_column(self, possible_names):
        """
        Finds the best matching column in the dataset.

        Strategy:
        1. Exact match
        2. Ends with keyword (e.g., Total Revenue -> Revenue)
        3. Contains keyword
        """

        columns = list(self.df.columns)

        # -----------------------------
        # Pass 1: Exact match
        # -----------------------------
        for name in possible_names:
            for column in columns:
                if column.lower() == name.lower():
                    return column

        # -----------------------------
        # Pass 2: Ends with keyword
        # Example:
        # Total Revenue -> Revenue
        # Item Type -> Type
        # -----------------------------
        for name in possible_names:
            for column in columns:
                if column.lower().endswith(name.lower()):
                    return column

        # -----------------------------
        # Pass 3: Contains keyword
        # -----------------------------
        for name in possible_names:
            for column in columns:
                if name.lower() in column.lower():
                    return column

        return None

    def get_date_range(self):

        date_col = self.find_column([
            "Date",
            "Order Date",
            "Invoice Date",
            "Ship Date",
            "Transaction Date"
        ])

        if not date_col:
            return None

        try:
            dates = pd.to_datetime(self.df[date_col])

            return {
                "column": date_col,
                "start": dates.min().strftime("%d %b %Y"),
                "end": dates.max().strftime("%d %b %Y"),
                "days": (dates.max() - dates.min()).days
            }

        except Exception:
            return None

















