# Business Climate Analysis

#### Resources

- VS Code 1.77
- Flask:
  - API routes:

    - /api/v1.0/precipitation
    - /api/v1.0/stations
    - /api/v1.0/tobs
    - /api/v1.0/temp/start/en
- Pandas
- SQLAlchemy
- MatPlotLib

### Overview

This analysis aims to assess the feasibility of opening a prospective surf and ice cream shop.
By examining temperatureand precipitation data in Oahu, we can determine if the business is sustainable year-round and identify opportunities to attract customers.

### Results

<table style='width: 80vw;'>
  <tr>
    <th></th>
    <th>June precip</th>
    <th>June temps</th>
    <th>December precip</th>
    <th>December temps</th>
  </tr>
  <tr>
    <td>count</td>
    <td>1574.00</td>
    <td>1700.00</td>
    <td>1405.00</td>
    <td>1517.00</td>
  </tr>
  <tr>
    <td>mean</td>
    <td>0.14</td>
    <td>74.94</td>
    <td>0.22</td>
    <td>71.04</td>
  </tr>
  <tr>
    <td>std</td>
    <td>0.34</td>
    <td>3.26</td>
    <td>0.54</td>
    <td>3.75</td>
  </tr>
  <tr>
    <td>min</td>
    <td>0.00</td>
    <td>64.00</td>
    <td>0.00</td>
    <td>56.00</td>
  </tr>
  <tr>
    <td>25%</td>
    <td>0.00</td>
    <td>73.00</td>
    <td>0.00</td>
    <td>69.00</td>
  </tr>
  <tr>
    <td>50%</td>
    <td>0.02</td>
    <td>75.00</td>
    <td>0.03</td>
    <td>71.00</td>
  </tr>
  <tr>
    <td>75%</td>
    <td>0.12</td>
    <td>77.00</td>
    <td>0.15</td>
    <td>74.00</td>
  </tr>
  <tr>
    <td>max</td>
    <td>4.43</td>
    <td>85.00</td>
    <td>6.42</td>
    <td>83.00</td>
  </tr>
</table>






June and December will give us a picture of the general summer and winter contditions of the island to best understand the potential weather highs and lows

Precipitation:

* In June usually rains less (0.14 inches) compared to December (0.21 inches). So June is a bit drier.
* December has more unpredictable weather when it comes to rain, with a high standard deviation (0.54 inches) compared to June's (0.34 inches).
* Sometimes in December, there can be really heavy rain, with the maximum recorded rainfall reaching 6.42 inches. In June, the maximum rainfall has reached 4.43 inches.

Temperature:

* June is typically warmer with an average temperature of 74.94°F, while December is a bit cooler at 71.04°F.
* Both June and December's temperatures have similar standard deviations, 3.26°F and  3.75°F respectively. So the temperatures in each month have a simlar spread.
* While the temperatures may usually stay within that spread, Decembers have gotten colder with a minimum temperature of 56°F. In June, the minimum is higher at 64°F.
* Both months can have hot days, but June tends to be slightly hotter with a maximum temperature of 85°F compared to December's 83°F.

# Conclusion

The analysis paints a positive picture for opening a surf and ice cream shop in Oahu. The weather patterns in June and December show consistent temperatures and manageable levels of rainfall, which is great. While there may be a few cooler or rainier days in winter months, overall, the conditions remain favorable for surfing and enjoying ice cream.

It's safe to say that opening a surf and ice cream shop in Oahu is a promising idea. So dive into this exciting venture, knowing that the weather is on your side!
