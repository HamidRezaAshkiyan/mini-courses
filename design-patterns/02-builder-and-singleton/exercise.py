import unittest


class SqlQueryBuilder:
    """Hands-on exercise: build a simple SELECT SQL query fluently.

    Example:
        SqlQueryBuilder("users")
            .select("id", "email")
            .where("active = 1")
            .limit(10)
            .build()
        => "SELECT id, email FROM users WHERE active = 1 LIMIT 10"
    """

    def __init__(self, table: str) -> None:
        self._table = table
        self._columns: list[str] = []
        self._conditions: list[str] = []
        self._limit: int | None = None

    def select(self, *columns: str) -> "SqlQueryBuilder":
        raise NotImplementedError("Store columns and return self")

    def where(self, condition: str) -> "SqlQueryBuilder":
        raise NotImplementedError("Append condition and return self")

    def limit(self, count: int) -> "SqlQueryBuilder":
        raise NotImplementedError("Validate count > 0, store limit, and return self")

    def build(self) -> str:
        raise NotImplementedError(
            "Default columns to '*' if none given; join WHERE conditions with ' AND '"
        )


class TestSqlQueryBuilder(unittest.TestCase):
    def test_example_instantiation(self) -> None:
        builder = SqlQueryBuilder("orders")
        self.assertIsNotNone(builder)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement SqlQueryBuilder")
    def test_default_select_all(self) -> None:
        sql = SqlQueryBuilder("users").build()
        self.assertEqual(sql, "SELECT * FROM users")

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement SqlQueryBuilder")
    def test_full_query(self) -> None:
        sql = (
            SqlQueryBuilder("users")
            .select("id", "name")
            .where("active = 1")
            .where("age >= 18")
            .limit(25)
            .build()
        )
        self.assertEqual(
            sql,
            "SELECT id, name FROM users WHERE active = 1 AND age >= 18 LIMIT 25",
        )


if __name__ == "__main__":
    unittest.main()
