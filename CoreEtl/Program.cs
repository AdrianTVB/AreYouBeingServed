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
			var meetingEntriesHDC = new LoadMeetingFile( ).LoadFile( @"..\..\..\DataSources\HDC2019.csv" );

			new MeetingAttendanceToDatabaseConverter( ).TransformAndInsert( meetingEntriesHDC );



			//var meetingEntriesNCC = new LoadMeetingFile( ).LoadFile( @"..\..\..\DataSources\ncc2019.csv" );

			//new MeetingAttendanceToDatabaseConverter( ).TransformAndInsert( meetingEntriesNCC );
		}
	}
}
