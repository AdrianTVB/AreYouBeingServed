using System;
using CoreEtl.Models.FromScraper;
using Domain.EntityFramework;
using System.Collections.Generic;

namespace CoreEtl.Transform.ToDatabase
{
	public class MeetingAttendanceToDatabaseConverter
	{
		public void TransformAndInsert( List<MeetingMetaData> meetingAttendances )
		{
			using ( creo_dbEntities dbContext = new creo_dbEntities( ) )
			{
				int i = 0;
				foreach ( MeetingMetaData meetingAttendance in meetingAttendances )
				{
					i++;
					Console.WriteLine( $"Processing {i} / {meetingAttendances.Count}" );

					// 1. Get or create organization
					if ( string.IsNullOrEmpty( meetingAttendance.Organisation ) )
					{
						Console.WriteLine( "Ignoring line in file...." );
						continue;
					}
					Organisation org = new ConverterHelper( ).GetOrCreateOrganisation( dbContext, meetingAttendance.Organisation );

					// 2. Get or create meeting
					Meeting meeting = new ConverterHelper( ).GetOrCreateMeeting( dbContext, meetingAttendance.Meeting, meetingAttendance.Date.Date, org );

					// 2. Get or create official
					if ( string.IsNullOrEmpty( meetingAttendance.Official ) )
					{
						continue;
					}

					Official official = new ConverterHelper( ).GetOrCreateOfficial( dbContext, meetingAttendance.Official, org );

					Attendance att = new Attendance { Meeting = meeting, Official = official };
					dbContext.Attendances.Add( att );
					dbContext.SaveChanges( );
				}
			}
		}
	}
}
