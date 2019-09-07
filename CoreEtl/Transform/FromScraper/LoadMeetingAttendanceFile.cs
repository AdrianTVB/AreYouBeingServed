using CoreEtl.Models.FromScraper;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CoreEtl.Transform.FromScraper
{
    class LoadMeetingAttendanceFile
    {
        public void LoadFile(string url)
        {
            using (var reader = new StreamReader(@"C:\Users\adtvb\Documents\ODM.csv"))
            {
                List<MeetingAttendance> Meetings = new List<MeetingAttendance>();
                List<string> listA = new List<string>();
                List<string> listB = new List<string>();
                List<string> listC = new List<string>();
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    listA.Add(values[0]);
                    listB.Add(values[1]);
                    listC.Add(values[2]);
                }
            }
        }
    }
}
