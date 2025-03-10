## Enable statistics
By default, statistics generation is *disabled* in PlantUML. If you want to enable statistic generation, you can either:
* Use ``-enablestats`` flag in the [command line](command-line)
* Use ``enablestats="true"`` setting with the [ANT task](ant-task)
* Globally set the environment variable ``PLANTUML_STATS`` to ``true``
* Call ``OptionFlags.getInstance().setEnableStats(true)`` from your Java code
Thoses statistics are very general. The goal is to measure PlantUML usage and performance and not to spy on users.
When statistics generation is on, a message is printed within the license to inform users about this.
(``@startuml/license/@enduml``).



## Statistics Report
You can generate statistics about your PlantUML usage either at XML or HTML format.

To do so, you can add ``-xmlstats`` or ``-htmlstats`` flag in the [command line](command-line).
A file *plantuml-stats.xml* or *plantuml-stats.html* will be written at the end of the process:

![](stats2.png)

If you want to generate statistics on the fly (rather than at the end of the process), you can use the flag ``-realtimestats``.

There is also a ``-loopstats`` flag in the command line that continuously prints to the console statistics about diagram generations.
This could be useful if you have some background daemon running PlantUML.

Some of those options are also available with the [ANT task](ant-task).


## Java Integration API
If you use PlantUML as a library, you can use the ``StatsUtils.getStats()`` methods that return a ``Stats`` object with all datas.

You can retrieve it to use it as you wish.

Here is a short class diagram about this API:

```plantuml
@startuml
class StatsUtil {
{static} +Stats getStats()
}
interface Stats {
+StatsTable getLastSessions()
+StatsTable getCurrentSessionByDiagramType()
+StatsTable getCurrentSessionByFormat()
+StatsTable getAllByDiagramType()
+StatsTable getAllByFormat()
}
StatsUtil -> Stats: build
Stats o--> "5" StatsTable: contains
enum StatsColumn {
SESSION_ID
VERSION
PARSED_COUNT
...
}
interface StatsTable {
+ Collection<StatsColumn> getColumnHeaders()
+ List<StatsLine> getLines()
}
StatsTable o-> StatsColumn: headers
StatsTable *--> StatsLine: contains
interface StatsLine {
}
interface StatsLine {
+Collection<StatsColumn> getColumnHeaders()
+Object getValue(StatsColumn column)
}
StatsLine o--> StatsColumn: headers
@enduml
```

*Implementation note:* The storage of historical data are provided through the
[Preference API](http://docs.oracle.com/javase/7/docs/technotes/guides/preferences/overview.html).



