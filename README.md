# aisle-developer-challenge

### Assumptions
* As there are some categories on which basic sales tax is exempted and there was no label or tag present in the input item. Thus, one of these tags ['book', 'medicine', 'food'] should be present in the input item to exempt an inptu item from tax.
```
For ex (these will work)
1 book at 12.49
1 Famous Five (book) at 78.09
1 packet of headache pills (medicine) at 9.75
1 box of imported chocolates (food) at 11.25
```
```
Can't determine whether they are exempted from tax
1 imported box of chocolates at 10.00
1 packet of headache pills: 9.75
```
* 2 packets of headache pills at 9.75 will mean that 1 packet cost 9.75 / 2 = 4.875

### Approach
* Taking input from a text file
* If a input line has two or more products mentioned, a logic is used so that the output will also have the same products in one line. In one line, it checks for a floating number, the next word after the floating number will obviously be the description of the next product. Thus, the floating numbers are considered to be the pivot where the array has been split.
* The calculations are done by rounding off to two decmal places.
* The sales tax and the total are printed n the last line.
