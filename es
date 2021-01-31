Help on method get_if_changed in module firebase_admin.db:

ggeett__iiff__cchhaannggeedd(etag) method of firebase_admin.db.Reference instance
    Gets data in this location only if the specified ETag does not match.
    
    Args:
      etag: The ETag value to be checked against the ETag of the current location.
    
    Returns:
      tuple: A 3-tuple consisting of a boolean, a decoded JSON value and an ETag. If the ETag
      specified by the caller did not match, the boolen value will be True and the JSON
      and ETag values would reflect the corresponding values in the database. If the ETag
      matched, the boolean value will be False and the other elements of the tuple will be
      None.
    
    Raises:
      ValueError: If the ETag is not a string.
      FirebaseError: If an error occurs while communicating with the remote database server.
