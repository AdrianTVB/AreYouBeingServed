using System.Collections.Generic;
using Creo.ViewModels.Official;

namespace Creo.ViewModels.MeetingAttendance
{
	public class MeetingAttendanceList
	{
		public List<OfficialListItem> Attendees { get; set; }
		public int MaxAttending { get; set; }
		public string Title { get; set; }
	}
}