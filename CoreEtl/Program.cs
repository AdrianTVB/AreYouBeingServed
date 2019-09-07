using CoreEtl.Transform.FromScraper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CoreEtl
{
	class Program
	{
		static void Main( string[ ] args )
        {
            new LoadMeetingFile().LoadFile("");
            new LoadMeetingAttendanceFile().LoadFile("");
        }
	}
}
