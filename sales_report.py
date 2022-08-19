"""Generate sales report showing total melons each salesperson sold."""

# dataset contains salesperson name, total amount of the order, and total number of melons sold

salespeople = []
melons_sold = []

# improvement for this loop function - better variable descriptions added
f = open('sales-report.txt')
for line in f:
    # the 2 lines below will take the dataset, remove whitespace and split out each column's value to create a list
    line = line.rstrip()
    entries = line.split('|')
     
    # below will identify the name of the salespersn & the number of melons sold
    salesperson = entries[0]
    melons = int(entries[2])

    # if the salesperson is already in the list ++ melons sold.
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        # otherwise, add the salesperson to the list & append melons sold
        salespeople.append(salesperson)
        melons_sold.append(melons)

# loop over lists and print summary for each salesperson & melons sold.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
