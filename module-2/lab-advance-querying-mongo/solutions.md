### Query 1
Filter : {name:"Babelgum"}

### Query 2
Filter : {number_of_employees:{$gt:5000}}
Sort: {number_of_employees:1}
Limit: 20

### Query 3
Filter : {founded_year:{$in: [2000,2001,2002,2003,2004,2005]}}
Project: {name:1, number_of_employees:1}

### Query 4
Filter : {$and:[{ipo:{$elemMatch:{valuation_amount:100000000}},{founded_year:{$lt:2010}}]}
Project: {name:1,ipo:1}

### Query 5
Filter :{$and:[{number_of_employees:{$lt:1000}}, {founded_year:{$lt:2005}}]}
Project: {number_of_employees:-1}
Limit: 10

### Query 6
Filter : {$ne:{$exists:partners}}

### Query 7
Filter : {category_code:null}

### Query 8
Filter : {$and:[{number_of_employees:{$gt:100}},{number_of_employees:{$lt:1000}}]}
Project: {name:1, number_of_employees:1}

### Query 9

Sort: {"ipo.valuation_amount":-1}

### Query 10
Project: {number_of_employees:1}
Sort:{number_of_employees:-1}

### Query 11
Filter : {founded_month:{$gt:6}}
Limit: 1000
### Query 12
Filter : {$and:[{founded_year:{$lt:2000}},{"ipo.valuation_amount":{$gt:10000000}}]}

### Query 13
Filter : {founded_year:{$gt:2010}}
Project: {name:1,acquisition:1} 
Sort: {"acquisition.price_amount":-1}

### Query 14
Project: {name:1,founded_year:1}
Sort: {founded_year:-1}

### Query 15
Filter : {founded_day:{$lte:7}}
Sort: {"acquisition.price_amount":1}

### Query 16
Filter : {$and:[{category_code:"web"},{number_of_employees:{$gt:4000}}]}
Sort: {number_of_employees:1}

### Query 17
Filter : {$and:[{"acquisition.price_amount":{$gt:10000000}},{"acquisition.price_currency_code":"EUR"}]}

### Query 18
Filter : {$and:[{"acquisition.acquired_month":{$gte:1}},{"acquisition.acquired_month":{$lte:3}}]}
Project: {name:1,acquisition:1}
Sort:

### Query 19
Filter : {$and:[{founded_year:{$gte:2000}},{founded_day:{$lte:2010}},{"acquisition.acquired_year":{$gte:2011}}]}
