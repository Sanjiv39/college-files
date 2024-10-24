// Collection
// Create
db.createCollection("Student");

// Display / Read
db.Student.find();

// Drop
db.Student.drop();

// Document

// Insert
db.Student.insertOne({
  first_name: "Radhika",
  last_name: "Sharma",
  date_of_birth: "1995-09-26",
  e_mail: "radhika_sharma.123@gmail.com",
  phone: "9848022338",
});

db.Student.insertMany([
  {
    first_name: "Radhika",
    last_name: "Sharma",
    date_of_birth: "1995-09-26",
    e_mail: "radhika_sharma.123@gmail.com",
    phone: "9000012345",
  },
  {
    first_name: "Rachel",
    last_name: "Christopher",
    date_of_birth: "1990-02-16",
    e_mail: "Rachel_Christopher.123@gmail.com",
    phone: "9000054321",
  },
  {
    first_name: "Fathima",
    last_name: "Sheik",
    date_of_birth: "1990-02-16",
    e_mail: "Fathima_Sheik.123@gmail.com",
    phone: "9000054321",
  },
]);

// Update
db.Student.updateOne(
  { first_name: "Radhika" },
  {
    $set: {
      date: Date(),
    },
  }
);
db.Student.updateMany(
  { first_name: "Radhika" },
  {
    $set: {
      date: Date(),
    },
  }
);

// Delete
db.Student.deleteOne(
  { first_name: "Radhika" }
);
db.Student.deleteMany(
  { first_name: "Radhika" }
);
