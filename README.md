# currency_conventer

## Stage 1: Cryptocurrencies are the new black

### Description
Today we start our new project. It will be a simple currency converter. Every person sometimes needs to convert one currency to another. But we need to start easy, so for now, all you need to do is to print "Meet a conicoin!" Please, make sure that the output formatting of your program follows the example output formatting.

###Objectives
Imagine that there is a cryptocurrency called `conicoin` ("coni" is just an anagram of the word "coin"). Greet conicoin as shown in the example below.

## Stage 2: Talking numbers

### Description
Holy moly! Suddenly you remember that back in 2008 you purchased several conicoins! Are you officially rich? Well, we need to find it out. You need to write a program that shows how much you can get after selling your conicoins. One conicoin is 100 dollars. Read your amount of the conicoins as the input, convert them into dollars, and output the result. Also, express your joy, it's important.

### Objectives
Find out if you are rich.

- [x] Input the amount of your conicoins.
- [x] Calculate the number of dollars you receive after the conversion. `1 conicoin = 100 dollars`, print the result as shown below.
- [x] `Woohoo! You are rich!`

## Stage 3: More interaction

### Description
We are going to make our program more complex. As you remember, the conicoin rate was fixed in the previous stage. But in the real world, things are different. It's time to write a program that takes your conicoins and an up-to-date conicoin exchange rate, then counts how many dollars you would get, and prints the result.

### Objectives
- [x] Get the number of conicoins from the user input.
- [x] Get the exchange rate from the user input.
- [x] Calculate and print the result.

## Stage 4: Going global
### Description
You can convert your conicoins into dollars, cool. What if you want a different currency? What if you're going to Morocco tomorrow? You'll need some dirhams, that's for sure. We need to improve our converter.

Take the imaginary exchange rates below and modify your program to work with 5 different currencies:

* `RUB – Russian Ruble; 1 conicoin = 2.98 RUB;`
* `ARS – Argentine Peso; 1 conicoin = 0.82 ARS;`
* `HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;`
* `AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;`
* `MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.`

Take the number of conicoins as the user input, сonvert it to the specified currencies, and round the result to two decimals using the Python built-in function. Notice that the input number can have a fractional part!

### Objectives
- [x] Get the number of conicoins from user input.
- [x] Print how much you will get in all five currencies mentioned above.

## Stage 5: JSON and the Rates

### Description
In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The (FloatRates)[http://www.floatrates.com/json-feeds.html] site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

### Objectives
There are many currency codes, for example, `RUB, ARS, HNL, AUD, MAD`, etc. Choose the one you like best and return the information about the exchange rates from the site specified above for only two currencies: `USD` and `EUR`.

- [x] Select one currency code, take it as the user input.
- [x] Make a request to http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json. Don't forget that you need to put the code in lowercase.
- [x] Print your result for `USD` and `EUR`. 

## Stage 6: Last but not least

### Description
At this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!

Parse the data from (FloatRates)[http://www.floatrates.com/json-feeds.html]. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.

Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you.

### Objectives
You're in the bank. Think about how much and what kind of currency you have.

- [x] Take the currency code, the amount of money the user has, and the currency code that the user wants to receive as the user input.
- [x] Retrieve the data from (FloatRates)[http://www.floatrates.com/json-feeds.html] as in the previous exercises.
- [x] Save the exchange rates for `USD` and `EUR`.
- [x] Read the currency to exchange for and the amount of money.
- [x] Take a look at the cache. Maybe you already have what you need?
- [x] If you have the currency in your cache, calculate the amount.
- [x] If not, get it from the site, and calculate the amount.
- [x] Save all the information to your cache.
- [x] Print the results.
- [x] Repeat steps 4-9 until there is no currency left to process.
