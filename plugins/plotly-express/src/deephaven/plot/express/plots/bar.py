from __future__ import annotations

from numbers import Number
from typing import Callable

from plotly import express as px

from deephaven.table import Table

from ._private_utils import validate_common_args, process_args
from ..shared import default_callback
from ..deephaven_figure import generate_figure, DeephavenFigure

# The functions in this file are exempt from the styleguide rule that types should not be in the description if there
# is a type annotation.


def bar(
    table: Table | None = None,
    x: str | list[str] | None = None,
    y: str | list[str] | None = None,
    by: str | list[str] | None = None,
    by_vars: str | list[str] = "color",
    color: str | list[str] | None = None,
    pattern_shape: str | list[str] | None = None,
    error_x: str | None = None,
    error_x_minus: str | None = None,
    error_y: str | None = None,
    error_y_minus: str | None = None,
    text: str | None = None,
    hover_name: str | None = None,
    labels: dict[str, str] | None = None,
    color_discrete_sequence: list[str] | None = None,
    color_discrete_map: str
    | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]]
    | dict[str | tuple[str], str]
    | None = None,
    pattern_shape_sequence: list[str] | None = None,
    pattern_shape_map: str
    | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]]
    | dict[str | tuple[str], str]
    | None = None,
    color_continuous_scale: list[str] | None = None,
    range_color: list[Number] | None = None,
    color_continuous_midpoint: Number | None = None,
    opacity: float | None = None,
    barmode: str = "relative",
    log_x: bool = False,
    log_y: bool = False,
    range_x: list[int] | None = None,
    range_y: list[int] | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    template: str | None = None,
    unsafe_update_figure: Callable = default_callback,
) -> DeephavenFigure:
    """Returns a bar chart

    Args:
      table: Table | None:  (Default value = None)
        A table to pull data from.
      x: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain x-axis values.
      y: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain y-axis values.
      by: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain values to plot the figure traces by.
        All values or combination of values map to a unique design. The variable
        by_vars specifies which design elements are used.
        This is overriden if any specialized design variables such as color are specified
      by_vars: str | list[str]:  (Default value = "color")
        A string or list of string that contain design elements to plot by.
        Can contain color and pattern_shape.
        If associated maps or sequences are specified, they are used to map by column values
        to designs. Otherwise, default values are used.
      color: str | list[str] | None: (Default value = None)
        A column or list of columns that contain color values.
        If only one column is passed, and it contains numeric values, the value
        is used as a value on a continuous color scale. Otherwise, the value is
        used for a plot by on color.
        See color_discrete_map for additional behaviors.
      pattern_shape: str | list[str] | None: (Default value = None)
        A column or list of columns that contain pattern shape values.
        The value is used for a plot by on pattern shape.
        See pattern_shape_map for additional behaviors.
      error_x: str | None: (Default value = None)
        A column with x error bar values.
        These form the error bars in both the positive and negative
        direction if error_x_minus is not specified, and the error bars in
        only the positive direction if error_x_minus is specified. None can be
        used to specify no error bars on the corresponding series.
      error_x_minus: str | None: (Default value = None)
        A column with x error bar values.
        These form the error bars in the negative direction,
        and are ignored if error_x is not specified.
      error_y: str | None: (Default value = None)
        A column with x error bar values.
        These form the error bars in both the positive and negative
        direction if error_y_minus is not specified, and the error bars in
        only the positive direction if error_y_minus is specified. None can be
        used to specify no error bars on the corresponding series.
      error_y_minus: str | None: (Default value = None)
        A column with y error bar values.
        These form the error bars in the negative direction,
        and are ignored if error_y is not specified.
      text: str | None:  (Default value = None)
        A column that contains text annotations.
      hover_name: str | None:  (Default value = None)
        A column that contains names to bold in the hover tooltip.
      labels: dict[str, str] | None:  (Default value = None)
        A dictionary of labels mapping columns to new labels.
      color_discrete_sequence: list[str] | None:  (Default value = None)
        A list of colors to sequentially apply to
        the series. The colors loop, so if there are more series than colors,
        colors will be reused.
      color_discrete_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None: (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to colors.
        If "identity", the values are taken as literal colors.
        If "by" or ("by", dict) where dict is as described above, the colors are forced to by
      pattern_shape_sequence: list[str] | None:  (Default value = None)
        A list of patterns to sequentially apply
        to the series. The patterns loop, so if there are more series than
        patterns, patterns will be reused.
      pattern_shape_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None: (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to patterns.
        If "identity", the values are taken as literal patterns.
        If "by" or ("by", dict) where dict is as described above, the patterns are forced to by
      color_continuous_scale: list[str] | None: (Default value = None)
        A list of colors for a continuous scale
      range_color: list[Number] | None: (Default value = None)
        A list of two numbers that form the endpoints of the color axis
      color_continuous_midpoint: Number | None: (Default value = None)
        A number that is the midpoint of the color axis
      opacity: float | None:  (Default value = None)
        Opacity to apply to all markers. 0 is completely transparent
        and 1 is completely opaque.
      barmode: str:  (Default value = 'relative')
        If 'relative', bars are stacked. If 'overlay', bars are drawn on top
        of each other. If 'group', bars are drawn next to each other.
      log_x: bool | list[bool]:  (Default value = False)
        A boolean or list of booleans that specify if
        the corresponding axis is a log axis or not. The booleans loop, so if there
        are more series than booleans, booleans will be reused.
      log_y: bool | list[bool]:  (Default value = False)
        A boolean or list of booleans that specify if
        the corresponding axis is a log axis or not. The booleans loop, so if there
        are more series than booleans, booleans will be reused.
      range_x: list[int] | list[list[int]] | None:  (Default value = None)
        A list of two numbers or a list of lists of two numbers
        that specify the range of the x axes. None can be specified for no range
        The ranges loop, so if there are more axes than ranges, ranges will
        be reused.
      range_y: list[int] | list[list[int]] | None:  (Default value = None)
        A list of two numbers or a list of lists of two numbers
        that specify the range of the y axes. None can be specified for no range
        The ranges loop, so if there are more axes than ranges, ranges will
        be reused.
      text_auto: bool | str:  (Default value = False)
        If True, display the value at each bar.
        If a string, specifies a plotly texttemplate.
      title: str | None: (Default value = None)
        The title of the chart
      template: str | None:  (Default value = None)
        The template for the chart.
      unsafe_update_figure: Callable:  (Default value = default_callback)
        An update function that takes a plotly figure
        as an argument and optionally returns a plotly figure. If a figure is
        not returned, the plotly figure passed will be assumed to be the return
        value. Used to add any custom changes to the underlying plotly figure.
        Note that the existing data traces should not be removed. This may lead
        to unexpected behavior if traces are modified in a way that break data
        mappings.

    Returns:
      DeephavenFigure: A DeephavenFigure that contains the bar chart

    """
    args = locals()

    return process_args(args, {"bar", "supports_lists"}, px_func=px.bar)


def _bar_polar(
    table: Table | None = None,
    r: str | None = None,
    theta: str | None = None,
    color_discrete_sequence: list[str] | None = None,
    pattern_shape_sequence: list[str] | None = None,
    # barnorm: str = None,
    barmode: str = "relative",
    direction: str = "clockwise",
    start_angle: int = 90,
    range_r: list[int] | None = None,
    range_theta: list[int] | None = None,
    log_r: bool = False,
    title: str | None = None,
    template: str | None = None,
    unsafe_update_figure: Callable = default_callback,
) -> DeephavenFigure:
    """

    Args:
      table: Table | None:  (Default value = None)
      r: str | None:  (Default value = None)
      theta: str | None:  (Default value = None)
      color_discrete_sequence: list[str] | None:  (Default value = None)
      pattern_shape_sequence: list[str] | None:  (Default value = None)
      # barnorm: str | None:  (Default value = None)
      barmode: str:  (Default value = 'relative')
      direction: str:  (Default value = 'clockwise')
      start_angle: int:  (Default value = 90)
      range_r: list[int] | None:  (Default value = None)
      range_theta: list[int] | None:  (Default value = None)
      log_r: bool:  (Default value = False)
      title: str | None:  (Default value = None)
      template: str | None:  (Default value = None)
      unsafe_update_figure: Callable:  (Default value = default_callback)

    Returns:

    """
    # todo: not yet implemented
    raise NotImplementedError("Not yet implemented")
    if isinstance(table, Table):
        args = locals()
        args["color_discrete_sequence_marker"] = args.pop("color_discrete_sequence")

        validate_common_args(args)

        return generate_figure(draw=px.bar_polar, call_args=args)


def timeline(
    table: Table | None = None,
    x_start: str | None = None,
    x_end: str | None = None,
    y: str | None = None,
    by: str | list[str] | None = None,
    by_vars: str | list[str] = "color",
    color: str | list[str] | None = None,
    pattern_shape: str | list[str] | None = None,
    text: str | None = None,
    hover_name: str | None = None,
    labels: dict[str, str] | None = None,
    color_discrete_sequence: list[str] | None = None,
    color_discrete_map: str
    | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]]
    | dict[str | tuple[str], str]
    | None = None,
    pattern_shape_sequence: list[str] | None = None,
    pattern_shape_map: str
    | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]]
    | dict[str | tuple[str], str]
    | None = None,
    color_continuous_scale: list[str] | None = None,
    range_color: list[Number] | None = None,
    color_continuous_midpoint: Number | None = None,
    opacity: float | None = None,
    range_x: list[int] | None = None,
    range_y: list[int] | None = None,
    title: str | None = None,
    template: str | None = None,
    unsafe_update_figure: Callable = default_callback,
):
    """Returns a timeline (otherwise known as a gantt chart)

    Args:
      table: Table | None:  (Default value = None)
        A table to pull data from.
      x_start: str | None:  (Default value = None)
        A column that contains starting x-axis values. Must be a `java.time.Instant` column.
      x_end: str | None:  (Default value = None)
        A column that contains ending x-axis values. Must be a `java.time.Instant` column.
      by: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain values to plot the figure traces by.
        All values or combination of values map to a unique design. The variable
        by_vars specifies which design elements are used.
        This is overriden if any specialized design variables such as color are specified
      by_vars: str | list[str]:  (Default value = "color")
        A string or list of string that contain design elements to plot by.
        Can contain color and pattern_shape.
        If associated maps or sequences are specified, they are used to map by column values
        to designs. Otherwise, default values are used.
      color: str | list[str] | None: (Default value = None)
        A column or list of columns that contain color values.
        If only one column is passed, and it contains numeric values, the value
        is used as a value on a continuous color scale. Otherwise, the value is
        used for a plot by on color.
        See color_discrete_map for additional behaviors.
      pattern_shape: str | list[str] | None: (Default value = None)
        A column or list of columns that contain pattern shape values.
        The value is used for a plot by on pattern shape.
        See pattern_shape_map for additional behaviors.
      y: str | None:  (Default value = None)
        A column that contains y-axis labels
      text: str | None:  (Default value = None)
        A column that contains text annotations.
      hover_name: str | None:  (Default value = None)
        A column that contains names to bold in the hover tooltip.
      labels: dict[str, str] | None:  (Default value = None)
        A dictionary of labels mapping columns to new labels.
      color_discrete_sequence: list[str] | None:  (Default value = None)
        A list of colors to sequentially apply to
        the series. The colors loop, so if there are more series than colors,
        colors will be reused.
      color_discrete_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None: (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to colors.
        If "identity", the values are taken as literal colors.
        If "by" or ("by", dict) where dict is as described above, the colors are forced to by
      pattern_shape_sequence: list[str] | None:  (Default value = None)
        A list of patterns to sequentially apply
        to the series. The patterns loop, so if there are more series than
        patterns, patterns will be reused.
      pattern_shape_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None: (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to patterns.
        If "identity", the values are taken as literal patterns.
        If "by" or ("by", dict) where dict is as described above, the patterns are forced to by
      color_continuous_scale: list[str] | None: (Default value = None)
        A list of colors for a continuous scale
      range_color: list[Number] | None: (Default value = None)
        A list of two numbers that form the endpoints of the color axis
      color_continuous_midpoint: Number | None: (Default value = None)
        A number that is the midpoint of the color axis
      opacity: float | None:  (Default value = None)
        Opacity to apply to all markers. 0 is completely transparent
        and 1 is completely opaque.
      range_x: list[int] | list[list[int]] | None:  (Default value = None)
        A list of two numbers or a list of lists of two numbers
        that specify the range of the x axes. None can be specified for no range
        The ranges loop, so if there are more axes than ranges, ranges will
        be reused.
      range_y: list[int] | list[list[int]] | None:  (Default value = None)
        A list of two numbers or a list of lists of two numbers
        that specify the range of the y axes. None can be specified for no range
        The ranges loop, so if there are more axes than ranges, ranges will
        be reused.
      title: str | None: (Default value = None)
        The title of the chart
      template: str:  (Default value = None)
        The template for the chart.
      unsafe_update_figure: Callable:  (Default value = default_callback)
        An update function that takes a plotly figure
        as an argument and optionally returns a plotly figure. If a figure is
        not returned, the plotly figure passed will be assumed to be the return
        value. Used to add any custom changes to the underlying plotly figure.
        Note that the existing data traces should not be removed. This may lead
        to unexpected behavior if traces are modified in a way that break data
        mappings.

    Returns:
      A DeephavenFigure that contains the timeline chart

    """
    args = locals()

    return process_args(args, {"bar", "preprocess_time"}, px_func=px.timeline)


def frequency_bar(
    table: Table | None = None,
    x: str | list[str] | None = None,
    y: str | list[str] | None = None,
    by: str | list[str] | None = None,
    by_vars: str | list[str] = "color",
    labels: dict[str, str] | None = None,
    color: str | list[str] | None = None,
    pattern_shape: str | list[str] | None = None,
    color_discrete_sequence: list[str] | None = None,
    color_discrete_map: dict[str | tuple[str], str] | None = None,
    pattern_shape_sequence: list[str] | None = None,
    pattern_shape_map: dict[str | tuple[str], str] | None = None,
    opacity: float | None = None,
    barmode: str = "relative",
    log_x: bool = False,
    log_y: bool = False,
    range_x: list[int] | None = None,
    range_y: list[int] | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    template: str | None = None,
    unsafe_update_figure: Callable = default_callback,
):
    """Returns a bar chart that contains the counts of the specified columns

    Args:
      table: Table | None:  (Default value = None)
        A table to pull data from.
      x: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain x-axis values.
        Only one of x or y can be specified. If x is specified, the bars
        are drawn vertically.
      y: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain y-axis values.
        Only one of x or y can be specified. If y is specified, the bars
        are drawn horizontally.
      by: str | list[str] | None:  (Default value = None)
        A column or list of columns that contain values to plot the figure traces by.
        All values or combination of values map to a unique design. The variable
        by_vars specifies which design elements are used.
        This is overriden if any specialized design variables such as color are specified
      by_vars: str | list[str]:  (Default value = "color")
        A string or list of string that contain design elements to plot by.
        Can contain color and pattern_shape.
        If associated maps or sequences are specified, they are used to map by column values
        to designs. Otherwise, default values are used.
      color: str | list[str] | None: (Default value = None)
        A column or list of columns that contain color values.
        The value is used for a plot by on color.
        See color_discrete_map for additional behaviors.
      pattern_shape: str | list[str] | None: (Default value = None)
        A column or list of columns that contain pattern shape values.
        The value is used for a plot by on pattern shape.
        See pattern_shape_map for additional behaviors.
      labels: dict[str, str] | None:  (Default value = None)
        A dictionary of labels mapping columns to new labels.
      color_discrete_sequence | None: list[str]:  (Default value = None)
        A list of colors to sequentially apply to
        the series. The colors loop, so if there are more series than colors,
        colors will be reused.
      color_discrete_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to colors.
      pattern_shape_sequence: list[str] | None:  (Default value = None)
        A list of patterns to sequentially apply
        to the series. The patterns loop, so if there are more series than
        patterns, patterns will be reused.
      pattern_shape_map:
        str | tuple[str, dict[str | tuple[str], dict[str | tuple[str], str]]] | dict[
            str | tuple[str], str] | None: (Default value = None)
        If dict, the keys should be strings of the column values (or a tuple
        of combinations of column values) which map to patterns.
      opacity: float | None:  (Default value = None)
        Opacity to apply to all markers. 0 is completely transparent
        and 1 is completely opaque.
      barmode: str:  (Default value = 'relative')
        If 'relative', bars are stacked. If 'overlay', bars are drawn on top
        of each other. If 'group', bars are drawn next to each other.
      log_x: bool
        A boolean that specifies if the corresponding axis is a log
        axis or not.
      log_y: bool
        A boolean that specifies if the corresponding axis is a log
        axis or not.
      range_x: list[int] | None:  (Default value = None)
        A list of two numbers that specify the range of the x-axis.
      range_y: list[int] | None:  (Default value = None)
        A list of two numbers that specify the range of the y-axis.
      text_auto: bool | str:  (Default value = False)
        If True, display the value at each bar.
        If a string, specifies a plotly texttemplate.
      title: str | None: (Default value = None)
        The title of the chart
      template: str | None:  (Default value = None)
        The template for the chart.
      unsafe_update_figure: Callable:  (Default value = default_callback)
        An update function that takes a plotly figure
        as an argument and optionally returns a plotly figure. If a figure is
        not returned, the plotly figure passed will be assumed to be the return
        value. Used to add any custom changes to the underlying plotly figure.
        Note that the existing data traces should not be removed. This may lead
        to unexpected behavior if traces are modified in a way that break data
        mappings.

    Returns:
      DeephavenFigure: A DeephavenFigure that contains the bar chart

    """

    if x and y:
        raise ValueError("Cannot specify both x and y")

    args = locals()

    return process_args(
        args, {"bar", "preprocess_freq", "supports_lists"}, px_func=px.bar
    )
