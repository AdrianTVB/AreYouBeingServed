using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Creo.ViewModels.Official;

namespace Creo.ViewModels.MeetingAttendance
{
	public class MeetingAttendanceList
	{
		public List<OfficialListItem> Attendees { get; set; }
	}
}