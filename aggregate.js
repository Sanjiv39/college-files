// a) Write a MongoDB Query to use sum , avg , min and max expression.

db.User.aggregate([
  { $group: { _id: "$by_user", num_tutorial: { $sum: "$likes" } } },
]);
db.User.aggregate([
  { $group: { _id: "$by_user", num_tutorial: { $avg: "$likes" } } },
]);
db.User.aggregate([
  { $group: { _id: "$by_user", num_tutorial: { $min: "$likes" } } },
]);
db.User.aggregate([
  { $group: { _id: "$by_user", num_tutorial: { $max: "$likes" } } },
]);

// b) Write a MongoDB query to use push and addToSet expression.

db.User.aggregate([{ $group: { _id: "$by_user", url: { $push: "$url" } } }]);
db.User.aggregate([
  { $group: { _id: "$by_user", url: { $addToSet: "$url" } } },
]);

// c) Write a MongoDB query to use first and last expression

db.User.aggregate([
  { $group: { _id: "$by_user", first_url: { $first: "$url" } } },
]);
db.User.aggregate([
  { $group: { _id: "$by_user", last_url: { $last: "$url" } } },
]);
