using CoreEtl.Transform.FromScraper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CoreEtl.Transform.ToDatabase;

namespace CoreEtl
{
	class Program
	{
		static void Main( string[ ] args )
        {
            var meetingEntries = new LoadMeetingFile().LoadFile("");

			new MeetingAttendanceToDatabaseConverter().TransformAndInsert( meetingEntries );
        }
	}
}
