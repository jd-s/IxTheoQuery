# IxTheoQuery

This is a little helper function to query the Index Theologicus (IXTheo, see https://ixtheo.de). IXTheo sadly does not provide a web API. Nevertheless, it is possible to query and gather data.

# Usage

Given a record URL (e.g. https://ixtheo.de/Record/109268283X) the function <code>getix(url)</code> will return a dictionary with title, keywords (if any) and publishing details. 

Given a query (e.g. "Josef Ernst Lukas") the function <code>getixuri(q)</code> will return the record URL of the **first** matching result or an empty string.


# License

IXTheoQuery is licensed under the GNU General Public License v3.0.
