using Domain.EntityFramework;
using System;
using System.Linq;
using Domain.EntityFramework;

namespace CoreEtl.Transform.ToDatabase
{
	public class ConverterHelper
	{
		public Organisation GetOrCreateOrganisation( creo_dbEntities dbContext, string orgName )
		{
			string orgNameRefined = orgName.ToLower( ).Trim( );
			Organisation org = dbContext.Organisations.FirstOrDefault( o => o.Name.ToLower( ) == orgNameRefined );
			if ( org == null )
			{
				dbContext.Organisations.Add( org = new Organisation { Name = orgName } );
				dbContext.SaveChanges( );
			}
			return org;
		}

		public Organisation GetOrCreateMeeting( creo_dbEntities dbContext, string meetingName, DateTime date )
		{
			string meetingNameRefined = meetingName.ToLower( ).Trim( );
			Organisation org = dbContext.Meetings.FirstOrDefault( o => o.Name.ToLower( ) == meetingNameRefined && o.);

			if (org != null)
				return org;

			dbContext.Organisations.Add( org = new Organisation( ) { Name = meetingName } );
			dbContext.SaveChanges( );
			return org;
		}
	}
}
