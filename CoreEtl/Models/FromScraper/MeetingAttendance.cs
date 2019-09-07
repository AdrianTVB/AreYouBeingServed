using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CoreEtl.Models.FromScraper
{
	public class MeetingAttendance
	{
		public string Organisation { get; set; }
		public DateTime Date { get; set; }
		public string Meeting { get; set; }
		public string Official { get; set; }
		public string Notes { get; set; }

	}
}
