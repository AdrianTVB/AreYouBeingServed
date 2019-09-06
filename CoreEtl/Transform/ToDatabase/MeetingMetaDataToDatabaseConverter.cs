using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CoreEtl.Models.FromScraper;
using Domain.EntityFramework;

namespace CoreEtl.Transform.ToDatabase
{
	public class MeetingMetaDataToDatabaseConverter
	{
		public void TransformAndInsert( List<MeetingMetaData> meetings )
		{
			using(creo_dbEntities dbContext = new creo_dbEntities(  ))
			{
				foreach ( MeetingMetaData meetingMetaData in meetings )
				{
					// 1. Get or create organisation
					Organisation org = new ConverterHelper().GetOrCreateOrganisation( dbContext, meetingMetaData.Organisation );
					
					// 2. Get or create meeting
					
				}
			}
		}
	}
}
