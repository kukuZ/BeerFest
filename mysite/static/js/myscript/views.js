function basic_radar(container, param)
{
    // Fill series s1 and s2.
    var data_list = [];
    var ticks_list = [];
    for(var i = 0; i < param.length; i++)
    {
        var tmp = [i, param[i][1]];
        var tmp2 = [i, param[i][0]];
        data_list.push(tmp);
        ticks_list.push(tmp2);
    }
    var
    s1 =
    {
        data: data_list 
    };
    var graph;
    var ticks;

    // Radar Labels
    ticks = ticks_list;

    // Draw the graph.
    graph = Flotr.draw(container, [s1],
            {
                radar:
                {
                    show: true
                },
                grid:
                {
                    circular: true,
                    minorHorizontalLines: true
                },
                yaxis:
                {
                    min: 0,
                    max: 10,
                    minorTickFreq: 2
                },
                xaxis:
                {
                    ticks: ticks
                }
            }
    );
};
