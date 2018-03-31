var RenderCandlesticks = function(name, candles, volume) {
  groupingUnits = [[
      'hour',                         // unit name
      [1, 4, 8, 12]                   // allowed multiples
    ],
    [
      'day',
      [1, 5, 14, 22]
    ],
    [
      'week',
      [1, 2, 4, 6, 12],
    ],
    [
      'month',
      [1, 4, 6, 12]
    ],
    [
      'year',
      [1, 4, 6, 10]
    ]
  ];
  return Highcharts.stockChart('candles', {
    rangeSelector: {
      selected: 1
    },
    title: {
      enabled: false
    },
    yAxis: [{
      labels: {
        align: 'right',
        x: -3
      },
      title: {
        text: 'Prices'
      },
      height: '60%',
      lineWidth: 2,
      resize: {
        enabled: true
      }
    },
    {
      labels: {
        align: 'right',
        x: -3
      },
      title: {
        text: 'Volume'
      },
      top: '65%',
      height: '35%',
      offset: 0,
      lineWidth: 2
    }],
    tooltip: {
      split: true
    },
    series: [{
      type: 'candlestick',
      name: name,
      data: candles,
      dataGrouping: {
        units: groupingUnits
      }
    },
    {
      type: 'column',
      name: 'Volume',
      data: volume,
      yAxis: 1,
      dataGrouping: {
        units: groupingUnits
      }
    }],
    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    }
  });
};
