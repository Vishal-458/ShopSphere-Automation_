import pytest

pytestmark = pytest.mark.database

def test_database_connection(db):

    result = db.execute_query(
        "SELECT 1"
    )

    assert result == [(1,)]


def test_create_orders_table(setup_orders_table):

    result = setup_orders_table.execute_query("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='orders'
    """)

    assert result == [("orders",)]


def test_insert_order(setup_orders_table):

    db = setup_orders_table

    db.execute_update(
        """
        INSERT INTO orders
        (order_id, customer_name, product_name, amount, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            1001,
            "Vishal",
            "Sauce Labs Backpack",
            29.99,
            "CONFIRMED"
        )
    )

    result = db.execute_query(
        """
        SELECT *
        FROM orders
        WHERE order_id = ?
        """,
        (1001,)
    )

    assert result == [
        (
            1001,
            "Vishal",
            "Sauce Labs Backpack",
            29.99,
            "CONFIRMED"
        )
    ]

def test_update_order_status(setup_orders_table):

    db = setup_orders_table

    db.execute_update(
        """
        INSERT INTO orders
        (order_id, customer_name, product_name, amount, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            1002,
            "Vishal",
            "Sauce Labs Bike Light",
            9.99,
            "PENDING"
        )
    )

    db.execute_update(
        """
        UPDATE orders
        SET status = ?
        WHERE order_id = ?
        """,
        ("CONFIRMED", 1002)
    )

    result = db.execute_query(
        """
        SELECT status
        FROM orders
        WHERE order_id = ?
        """,
        (1002,)
    )

def test_delete_order(setup_orders_table):

    db = setup_orders_table

    db.execute_update(
        """
        INSERT INTO orders
        (order_id, customer_name, product_name, amount, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            1003,
            "Vishal",
            "Sauce Labs Bolt T-Shirt",
            15.99,
            "CANCELLED"
        )
    )

    db.execute_update(
        """
        DELETE FROM orders
        WHERE order_id = ?
        """,
        (1003,)
    )

    result = db.execute_query(
        """
        SELECT *
        FROM orders
        WHERE order_id = ?
        """,
        (1003,)
    )

    assert result == []

def test_order_total(setup_orders_table):

    db = setup_orders_table

    orders = [
        (2001, "Vishal", "Backpack", 29.99, "CONFIRMED"),
        (2002, "Vishal", "Bike Light", 9.99, "CONFIRMED"),
        (2003, "Vishal", "T-Shirt", 15.99, "CONFIRMED")
    ]

    for order in orders:
        db.execute_update(
            """
            INSERT INTO orders
            (order_id, customer_name, product_name, amount, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            order
        )

    result = db.execute_query(
        """
        SELECT COUNT(*), SUM(amount)
        FROM orders
        WHERE status = ?
        """,
        ("CONFIRMED",)
    )

    count, total = result[0]

    assert count == 3
    assert round(total, 2) == 55.97

def test_orders_sorted_by_amount(setup_orders_table):

    db = setup_orders_table

    orders = [
        (3001, "Vishal", "Backpack", 29.99, "CONFIRMED"),
        (3002, "Vishal", "Bike Light", 9.99, "CONFIRMED"),
        (3003, "Vishal", "T-Shirt", 15.99, "CONFIRMED")
    ]

    for order in orders:
        db.execute_update(
            """
            INSERT INTO orders
            (order_id, customer_name, product_name, amount, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            order
        )

    result = db.execute_query(
        """
        SELECT amount
        FROM orders
        ORDER BY amount DESC
        """
    )

    amounts = [row[0] for row in result]

    assert amounts == [29.99, 15.99, 9.99]

def insert_shop_data(db):

    db.execute_update(
        """
        INSERT INTO customers
        (customer_id, name, email)
        VALUES (?, ?, ?)
        """,
        (1, "Vishal", "vishal@test.com")
    )

    db.execute_update(
        """
        INSERT INTO products
        (product_id, name, price)
        VALUES (?, ?, ?)
        """,
        (101, "Sauce Labs Backpack", 29.99)
    )

    db.execute_update(
        """
        INSERT INTO products
        (product_id, name, price)
        VALUES (?, ?, ?)
        """,
        (102, "Sauce Labs Bike Light", 9.99)
    )

    db.execute_update(
        """
        INSERT INTO shop_orders
        (order_id, customer_id, product_id, quantity, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (5001, 1, 101, 2, "CONFIRMED")
    )

def test_order_customer_product_join(setup_shop_tables):

    db = setup_shop_tables

    insert_shop_data(db)

    result = db.execute_query("""
        SELECT
            o.order_id,
            c.name,
            p.name,
            o.quantity,
            p.price,
            o.status
        FROM shop_orders o
        INNER JOIN customers c
            ON o.customer_id = c.customer_id
        INNER JOIN products p
            ON o.product_id = p.product_id
        WHERE o.order_id = ?
    """, (5001,))

    assert result == [
        (
            5001,
            "Vishal",
            "Sauce Labs Backpack",
            2,
            29.99,
            "CONFIRMED"
        )
    ]

def test_order_total_from_database(setup_shop_tables):

    db = setup_shop_tables

    insert_shop_data(db)

    result = db.execute_query("""
        SELECT
            o.quantity,
            p.price,
            o.quantity * p.price AS total
        FROM shop_orders o
        INNER JOIN products p
            ON o.product_id = p.product_id
        WHERE o.order_id = ?
    """, (5001,))

    quantity, price, total = result[0]

    assert quantity == 2
    assert price == 29.99
    assert round(total, 2) == 59.98

def test_customer_order_count(setup_shop_tables):

    db = setup_shop_tables

    insert_shop_data(db)

    result = db.execute_query("""
        SELECT
            c.name,
            COUNT(o.order_id) AS order_count
        FROM customers c
        LEFT JOIN shop_orders o
            ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name
    """)

    assert result == [
        ("Vishal", 1)
    ]

def test_customer_without_order(setup_shop_tables):

    db = setup_shop_tables

    insert_shop_data(db)

    db.execute_update(
        """
        INSERT INTO customers
        (customer_id, name, email)
        VALUES (?, ?, ?)
        """,
        (2, "Rahul", "rahul@test.com")
    )

    result = db.execute_query("""
        SELECT
            c.name,
            COUNT(o.order_id)
        FROM customers c
        LEFT JOIN shop_orders o
            ON c.customer_id = o.customer_id
        WHERE c.customer_id = ?
        GROUP BY c.customer_id, c.name
    """, (2,))

    assert result == [
        ("Rahul", 0)
    ]