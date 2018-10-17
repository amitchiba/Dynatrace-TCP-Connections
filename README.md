# Dynatrace-TCP-Connections
A Dynatrace OneAgent Local Plugin that checks the output of the Netstat command and pushes this information to Dynatrace. This Agent is specific for Windows

## Information
The Host Entity is used to capture this information.
You will be able to view the data by using either an API call in Dynatrace, or by making use of a Custom Chart.

Search for "netstat" when creating the custom chart to plot the metrics from the plugin.


## Installation
OneAgent Plugins need to get installed both, on your Tenant and on the host(s) they are supposed to collect data for - mainly for security reasons. NO third party code is getting executed by your OneAgent unless your Tenant and your Agent agree on the authenticity of your plugin.
This is why you need to install any custom plugin, in addition to your Tenant, on selected Hosts, that have OneAgent running and are supposed to execute your plugin.
### Installation on your Dynatrace Tenant
* Package the file `plugin.json` and `tcp_connections_plugin.py` into a zip archive named `custom.python.tcp_connections_plugin.zip`.
* Navigate in the Web Interface of your Tenant to `Settings / Monitoring / Monitored Technologies` and select the tab `Custom Plugins`.
* Click on the button `Upload Plugin` and install your zip archive on your tenant.
* Select the new entry in the list of your plugins and promote it from Staging to Production
### Installation on your monitored host
* Create a folder name `custom.python.tcp_connections_plugin` within `C:\Program Files (x86)\dynatrace\oneagent\plugin_deployment`
* Copy `plugin.json` and `tcp_connections_plugin.py` into that folder
* Restart Oneagent 
### Visualizing the data
To visualize the data, you can click on custom charts, and search for netstat. All the metrics returned by this plugin will be available for seleection

#### Notes
I am a Noob and this was my first attempt at creating a plugin. Please feel free to suggest improvements to the code"# Dynatrace-TCP-Connections" 
