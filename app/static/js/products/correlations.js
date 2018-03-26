var RenderCorrelations = function(name, symbols, negativeCorrelations, positiveCorrelations) {

  return Highcharts.chart("correlations", {

      chart: {
          polar: true,
          type: 'line'
      },
      title: {
          text: name,
          x: -80
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
          align: 'right',
          verticalAlign: 'top',
          y: 70,
          layout: 'vertical'
      },
      series: [{
          name: 'Negative Correlations',
          data: negativeCorrelations,
          pointPlacement: 'on'
      }, {
          name: 'Positive Correlations',
          data: positiveCorrelations,
          pointPlacement: 'on'
      }]
  });
};
