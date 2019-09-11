using System;
using Creo.ViewModels.Official;

namespace Creo.ViewModels.MeetingAttendance
{
	public class MeetingAttendanceListItem
	{
		public int Id { get; set; }
		public OfficialListItem Official { get; set; }
		public string Organisation { get; set; }
		public DateTime Date { get; set; }
		public string Meeting { get; set; }
	}
}