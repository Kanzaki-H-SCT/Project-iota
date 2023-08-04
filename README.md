### API Refer

The following examples are available for the new Chats service:

* 'chatMid' equal to previous version 'group.id' *
* Left side is Chats Service, while right side is for comparing to previous group service. *

# Chats Service Explain
- `getChats([chatMid]).chats[0]` - getGroup. >> In case, [] is a list.
- `getChatV2(chatMid)` - getGroup.
  

    Above functions can be run with following attributes:
     - type
     - chatMid
     - createdTime
     - notificationDisabled
     - favoriteTimestamp
     - chatName
     - picturePath
     - extra
         - extra also contain different attributes:
             - groupExtra
                 - creator
                 - preventedJoinByTicket
                 - invitationTicket
                 - memberMids
                 - inviteeMids
                 - peerExtra
  
> Example Request Result: Chat(type=0, chatMid='', createdTime='', notificationDisabled=False, favoriteTimestamp=0, chatName='', picturePath='', extra=Extra(groupExtra=GroupExtra(creator='', preventedJoinByTicket=True, invitationTicket='', memberMids={'': }, inviteeMids={'': }), peerExtra=None))

  

- `updateChat(chatMid, UpdatedAttribute)` - updateGroup.
  
      > UpdatedAttribute can be determined as follow:
          NAME = 1
          PICTURE_STATUS = 2
          PREVENTED_JOIN_BY_TICKET = 4
          NOTIFICATION_SETTING = 8
          INVITATION_TICKET = 16
          FAVORITE_TIMESTAMP = 32
          CHAT_TYPE = 64
  
  
   
- `deleteOtherFromChat(chatMid, [userMid])` - kickoutFromGroup.
- `deleteSelfFromChat` - leaveGroup.

  Following is all the new Chats Service function, while there's no compare anymore.

  - getChatRoomAnnouncementsBulk
  - getChatRoomAnnouncements
  - createChatRoomAnnouncement
  - removeChatRoomAnnouncement
  - acceptChatInvitationByTicket
  - acceptChatInvitation
  - cancelChatInvitation
  - createChat
  - findChatByTicket
  - getAllChatMids
  - inviteIntoChat
  - reissueChatTicket
  - rejectChatInvitation

  Please read the entire README.md file, which is a respect for all of the developer, modifier, and all of the user participated in this project.
  
### CTCoreTeam & Thanks

The Group service has been discontinued and replaced by the Chats service. The API has been fixed to accommodate these changes and includes the necessary endpoints for the new service.

LINEPY is originally public by Fadhiil Rachman. 

* Special thanks to Github user: ratezpro - Provided examples of Chat service *

CT Core Team Fixed all issue of Linepy with adding Chats Service, also giving a tutorial.

Appreciate to all Github Resouces which related to LINEPY. All of them may ever help this repository.

This repository contains the updated API for the discontinued Group service and the introduction of the new Chats service.


# Usage & Legal Clarification

Please note the following legal information regarding the usage of this API:

1. **Disclaimer of Liability:** The API provided in this repository is offered "as is" without any warranty or guarantee of any kind. The developers of this API shall not be held liable for any damages or losses arising from its use.

2. **Usage Compliance:** Users of this API are solely responsible for ensuring their compliance with all applicable laws, regulations, and policies of their jurisdiction. It is the user's responsibility to obtain any necessary permissions, licenses, or consents required for their specific use case.

3. **Data Privacy and Security:** This API may involve the processing of personal data. Users are responsible for handling any personal data in compliance with applicable data protection laws and regulations. It is strongly recommended to implement appropriate security measures to protect sensitive information.

4. **Intellectual Property:** All intellectual property rights related to this API and its documentation belong to the respective owners. Users are granted a limited license to use the API strictly for its intended purpose as described in the documentation. Unauthorized reproduction, modification, or distribution of the API is strictly prohibited.

5. **Third-Party Dependencies:** This API may utilize third-party libraries or services. The respective terms and conditions of these dependencies apply and users are encouraged to review and comply with them.

It is important to consult with legal professionals or your organization's legal department to ensure compliance with all relevant laws and regulations specific to your use case.

Please refer to the API documentation for detailed information on how to use each endpoint.

## Contributing

If you would like to contribute to this project, please contact me directly via email or discord: .ct_

## License

This project is licensed under the [BSD-3 License](LICENSE).
