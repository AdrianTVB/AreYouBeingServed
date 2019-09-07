using CoreEtl.Models.FromScraper;
using Domain.EntityFramework;
using System.Collections.Generic;

namespace CoreEtl.Transform.ToDatabase
{
	public class MeetingMetaDataToDatabaseConverter
	{
		public void TransformAndInsert( List<MeetingMetaData> meetings )
		{
			using ( creo_dbEntities dbContext = new creo_dbEntities( ) )
			{
				foreach ( MeetingMetaData meetingMetaData in meetings )
				{
					// 1. Get or create organization
					Organisation org = new ConverterHelper( ).GetOrCreateOrganisation( dbContext, meetingMetaData.Organisation );

					// 2. Get or create meeting
					Meeting meeting = new ConverterHelper( ).GetOrCreateMeeting( dbContext, meetingMetaData.Meeting, meetingMetaData.Date.Date, org );

				}
			}
		}
	}
}
