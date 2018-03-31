var RenderCorrelations = function(name, symbols, negativeCorrelations, positiveCorrelations) {

  return Highcharts.chart("correlations", {

      chart: {
          polar: true,
          type: 'line'
      },
      title: {
          text: null,
          enabled: false
      },
      pane: {
          size: '80%'
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
          shared: true,
          pointFormat: '<span><b style="color:{series.color}">{point.y:,.2f}</b><br/>'
      },
      legend: {
          enabled: false
      },
      series: [{
          name: 'Negative Correlations',
          data: negativeCorrelations,
          pointPlacement: 'on'
      }, {
          name: 'Positive Correlations',
          data: positiveCorrelations,
          pointPlacement: 'on'
      }],
      credits: {
        enabled: false
      },
      exporting: {
        enabled: false
      }
  });
};
