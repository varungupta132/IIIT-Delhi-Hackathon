CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL,
    UnitPrice REAL NOT NULL,
    QuantityInStock INTEGER NOT NULL,
    SupplierID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Insert 30 sample products into the Products table
INSERT INTO Products (ProductName, Category, UnitPrice, QuantityInStock, SupplierID)
VALUES
-- Electronics
('Smartphone X', 'Electronics', 699.99, 50, 1),
('Laptop Pro', 'Electronics', 1299.99, 30, 1),
('Wireless Earbuds', 'Electronics', 99.99, 100, 2),
('4K Smart TV', 'Electronics', 799.99, 20, 3),
('Gaming Console', 'Electronics', 499.99, 40, 4),

-- Clothing
('Men\'s T-Shirt', 'Clothing', 19.99, 200, 2),
('Women\'s Jeans', 'Clothing', 39.99, 150, 2),
('Kids\' Jacket', 'Clothing', 29.99, 100, 3),
('Unisex Hoodie', 'Clothing', 49.99, 120, 4),
('Running Shoes', 'Clothing', 59.99, 80, 5),

-- Groceries
('Organic Apples', 'Groceries', 2.99, 500, 1),
('Whole Grain Bread', 'Groceries', 3.49, 300, 2),
('Fresh Milk', 'Groceries', 1.99, 400, 3),
('Canned Beans', 'Groceries', 1.49, 600, 4),
('Olive Oil', 'Groceries', 9.99, 200, 5),

-- Home Appliances
('Blender', 'Home Appliances', 49.99, 60, 1),
('Microwave Oven', 'Home Appliances', 89.99, 40, 2),
('Vacuum Cleaner', 'Home Appliances', 129.99, 30, 3),
('Air Purifier', 'Home Appliances', 199.99, 20, 4),
('Coffee Maker', 'Home Appliances', 59.99, 50, 5),

-- Toys
('LEGO Set', 'Toys', 29.99, 100, 1),
('Remote Control Car', 'Toys', 19.99, 150, 2),
('Board Game', 'Toys', 24.99, 80, 3),
('Stuffed Animal', 'Toys', 14.99, 200, 4),
('Puzzle', 'Toys', 9.99, 250, 5),

-- Miscellaneous
('Backpack', 'Miscellaneous', 39.99, 120, 1),
('Water Bottle', 'Miscellaneous', 12.99, 300, 2),
('Sunglasses', 'Miscellaneous', 29.99, 150, 3),
('Umbrella', 'Miscellaneous', 19.99, 200, 4),
('Notebook', 'Miscellaneous', 4.99, 500, 5);