import os, re
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.selectors import HostSelector
from subprocess import check_output


class tcpCountPlugin(BasePlugin):

	def initialize(self, **kwargs):
		self.json_config = kwargs["json_config"]
		self.metrics = kwargs["json_config"]["metrics"]
		
	def query(self, **kwargs):
		
		host_id =  self.query_snapshot.host_id
		
		for metric in self.metrics:
			timeseries = None
			metric_key = None
			outVal = 0
			result = check_output("netstat -an", shell=True)
			output = result.decode(encoding='utf-8')
		
			try:
				timeseries = metric["timeseries"]
			except KeyError:
				continue
				
			try:
				metric_key = timeseries["key"]
			except KeyError:
				continue
			
			if metric_key == "tcpEstablished":
				estCount=0
				for line in output.split("\n"):
					if "ESTABLISHED" in line:
						estCount=estCount+1
				outVal = estCount

			if metric_key == "tcpTimeWait":
				twCount=0
				for line in output.split("\n"):
					if "TIME" in line:
						twCount=twCount+1
				outVal = twCount

			if metric_key == "tcpSynSent":
				tssCount=0
				for line in output.split("\n"):
					if "SYN_SENT" in line:
						tssCount=tssCount+1
				outVal = tssCount

			if metric_key == "tcpSynReceived":
				tsrCount=0
				for line in output.split("\n"):
					if "SYN_REC" in line:
						tsrCount=tsrCount+1
				outVal = tsrCount

			if metric_key == "tcpListening":
				tlCount=0
				for line in output.split("\n"):
					if "LISTENING" in line:
						tlCount=tlCount+1
				outVal = tlCount

			if metric_key == "tcpCloseWait":
				tcwCount=0
				for line in output.split("\n"):
					if "CLOSE_W" in line:
						tcwCount=tcwCount+1
				outVal = tcwCount

			if metric_key == "tcpFinWait":
				tfwCount=0
				for line in output.split("\n"):
					if "FIN_WAIT" in line:
						tfwCount=tfwCount+1
				outVal = tfwCount

			if metric_key == "tcpLastAck":
				tlaCount=0
				for line in output.split("\n"):
					if "LAST_ACK" in line:
						tlaCount=tlaCount+1
				outVal = tlaCount

			if metric_key == "tcpClosed":
				tcCount=0
				for line in output.split("\n"):
					if "CLOSED" in line:
						tcCount=tcCount+1
				outVal = tcCount

			outVal = float(outVal)

			self.results_builder.absolute(key=metric_key,value=outVal,entity_id=host_id)