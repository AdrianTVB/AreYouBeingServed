using CoreEtl.Models.FromScraper;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CoreEtl.Transform.FromScraper
{
    class LoadMeetingFile
    {
        public List<MeetingMetaData> LoadFile(string url)
        {
            using (var reader = new StreamReader(@"C:\Users\adtvb\Documents\ODM.csv"))
            {
                List<MeetingMetaData> Meetings = new List<MeetingMetaData>();

                while (!reader.EndOfStream)
                {
                    MeetingMetaData Meeting = new MeetingMetaData();
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    Meeting.Organisation = values[0];
                    Meeting.Date = values[1];
                    Meeting.Meeting = values[2];

                    Meetings.Add(Meeting);

                }

				return Meetings;
            }

        }
    }
}
