using CoreEtl.Models.FromScraper;
using System;
using System.Collections.Generic;
using System.Globalization;
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
            using (var reader = new StreamReader(@"C:\Users\adtvb\Documents\ncc2019.csv"))
            {
                List<MeetingMetaData> Meetings = new List<MeetingMetaData>();

                while (!reader.EndOfStream)
                {
                    MeetingMetaData Meeting = new MeetingMetaData();
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    Meeting.Organisation = values[0];
                    Meeting.Date = DateTime.ParseExact(values[1], "dd/MM/yyyy",
                                           CultureInfo.InvariantCulture);
                    Meeting.Meeting = values[2];
                    Meeting.Official = values[3];
                    Meeting.Notes = values[5];

                    Meetings.Add(Meeting);

                }

				return Meetings;
            }

        }
    }
}
