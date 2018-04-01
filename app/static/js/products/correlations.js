var RenderCorrelations = function(name, symbols, negativeCorrelations, positiveCorrelations) {

  return Highcharts.chart("correlations", {

      credits: {
        enabled: false
      },
      exporting: {
        enabled: false
      },
      legend: {
        enabled: false
      },
      title: {
          text: null,
          enabled: false
      },
      chart: {
        polar: true,
        type: 'line'
      },
      xAxis: {
          categories: symbols,
          tickmarkPlacement: 'on',
          lineWidth: 0
      },
      yAxis: {
          gridLineInterpolation: 'polygon',
          lineWidth: 0,
          min: 0
      },
      tooltip: {
          shared: false,
          pointFormat: '<span><b style="color:{series.color}">{point.y:,.2f}</b><br/>'
      },
      plotOptions: {
        series: {
          marker: {
            enabled: false
          }
        }
      },
      series: [
        {
          name: 'Positive Correlations',
          data: positiveCorrelations,
          pointPlacement: 'on',
          color: '#38BB9B'
        },
        {
          name: 'Negative Correlations',
          data: negativeCorrelations,
          pointPlacement: 'on',
          color: '#D66F37'
        }
      ]
  });
};
