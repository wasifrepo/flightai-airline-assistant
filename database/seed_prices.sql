DROP TABLE IF EXISTS prices;

CREATE TABLE prices (
  city TEXT PRIMARY KEY,
  price INTEGER NOT NULL
);

INSERT INTO prices (city, price) VALUES
  ('paris', 450),
  ('london', 520),
  ('lahore', 680),
  ('karachi', 650),
  ('dubai', 620),
  ('new york', 950),
  ('tokyo', 1100),
  ('singapore', 780);
