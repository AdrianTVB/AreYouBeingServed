using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Creo.ViewModels.MeetingAttendance
{
	public class MeetingAttendanceListItem
	{
		public int Id { get; set; }
		public string Organisation { get; set; }
		public string Date { get; set; }
		public string Meeting { get; set; }
	}
}