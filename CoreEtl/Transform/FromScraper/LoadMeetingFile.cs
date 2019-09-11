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
		public List<MeetingMetaData> LoadFile( string url )
		{
			using ( var reader = new StreamReader( url ) )
			{
				List<MeetingMetaData> Meetings = new List<MeetingMetaData>( );

				while ( !reader.EndOfStream )
				{
					MeetingMetaData Meeting = new MeetingMetaData( );
					var line = reader.ReadLine( );
					var values = line.Split( ',' );

					if ( values[ 0 ] == "Organisation" )
					{
						continue;
					}
					int i = 0;
					Meeting.Organisation = values[ i++ ];
					if ( !string.IsNullOrEmpty( values[ i ] ) )
					{
						if ( values[ i ][ i ] == '/' )
						{
							values[ i ] = '0' + values[ i ];
						}
						Meeting.Date = DateTime.ParseExact( values[ i ], "dd/MM/yyyy",
											   CultureInfo.InvariantCulture );
					}
					else
					{
						continue;
					}

					i++;
					Meeting.Meeting = values[ i++ ];
					Meeting.NameRaw = values[ i++ ];
					Meeting.Official = values[ i++ ];
					//Meeting.LastName = values[ i++ ];
					Meeting.VideoLink = values[ i++ ];
					Meeting.OrganisationForOfficial = values[ i++ ];
					Meetings.Add( Meeting );

				}

				Console.WriteLine( $"Loaded in {Meetings.Count} lines in file." );
				return Meetings;
			}

		}
	}
}
