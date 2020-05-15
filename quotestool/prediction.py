def predict(smc,eau):
    import os, pandas, matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    dataset = pandas.read_csv('quotestool/750 Won Or Not.csv')
    array = dataset.values
    X = array[:,0:3]
    Y = array[:,3]
    rfc = RandomForestClassifier()
    rfc.fit(X,Y)
    lor = LogisticRegression()
    lor.fit(X,Y)

    salesPredictions = []    
    for margin in range(50,710,25):
        margin = margin/10
        price = 100*smc/(100 - margin)
        salesPrediction = rfc.predict([[eau, price, smc]])
        if salesPrediction > 0:
            salesPredictions += [[margin, price/100, smc/100]]

    sdpQ = []
    sdpP = []
    sdpS = []
    sdpM = []
    udpQ = []
    udpP = []
    udpS = []
    udpM = []
    for each in array:
        dpQuantity = each[0]
        dpPrice = each[1]
        dpSMC = each[2]
        dpMargin = (1 - dpSMC/dpPrice)*100
        dpSales = each[3]
        if eau*0.8 < dpQuantity < eau*1.2 and smc*0.8 < dpSMC < smc*1.2:
            if dpSales < 1:
                udpQ += [dpQuantity]
                udpS += [dpSMC/100]
                udpP += [dpPrice/100]
                udpM += [dpMargin]  
            if dpSales > 0:
                sdpQ += [dpQuantity]
                sdpS += [dpSMC/100]
                sdpP += [dpPrice/100]
                sdpM += [dpMargin]
    plt.clf()
    plt.plot(udpQ,udpM,'ro',sdpQ,sdpM,'go')
    plt.title('Past quotes at Similar SMC & Quantity')
    plt.xlabel('Quantity')
    plt.ylabel('% Margin')
    plt.savefig('quotestool/static/quotestool/otherstuff.png')
    return salesPredictions

def makePriceMarginList(smc):
    priceMarginList = []
    for margin in range(5,71,5):
        priceMarginList += [[margin, round(smc/(100-margin),2)]]
    return priceMarginList
        