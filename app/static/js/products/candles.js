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
    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    },
    plotOptions: {
        candlestick: {
            color: '#D66F37',
            upColor: '#38BB9B',
            lineColor: '#1D1F21',
            lineWidth: 1
        }
    },
    rangeSelector: {
      selected: 1
    },
    title: {
      text: null,
      enabled: false
    },
    xAxis: {
      gridLineWidth: 1
    },
    yAxis: {
      title: {
        text: 'Prices'
      },
      resize: {
        enabled: true
      }
    },
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
    }]
  });
};
