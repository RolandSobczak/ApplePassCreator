import pytest


@pytest.fixture
def text_file_content() -> str:
    return """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae vestibulum risus. Donec ut metus finibus, vehicula sem nec, pretium turpis. Donec id justo mollis, posuere nibh vitae, ultricies felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed vel ultricies sapien, non tincidunt orci. Vestibulum vehicula dui eget urna condimentum, at fringilla ex placerat. Vivamus tincidunt erat ut finibus ornare. Mauris et condimentum odio, molestie elementum odio.

    Maecenas ac lacinia magna. Vivamus magna metus, blandit non vulputate id, facilisis sed risus. Fusce eu aliquet urna, et dignissim ex. Proin blandit facilisis felis, non gravida enim fermentum sed. Nulla aliquet augue id fringilla vehicula. Aenean consequat risus at libero volutpat molestie. Duis lectus mauris, mollis a bibendum auctor, maximus id velit. Mauris tempor eget mauris in pulvinar. Suspendisse vitae lectus in felis rutrum placerat. Donec vel orci ex. Proin euismod nunc nisl, eget rhoncus augue commodo ut. Nam tincidunt tortor metus, sit amet fermentum tellus lacinia et. Quisque laoreet diam sollicitudin enim lobortis, id congue elit bibendum.

    Nulla fringilla dictum tortor, non lacinia neque placerat eget. Nulla facilisi. Etiam porttitor finibus risus sit amet malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc venenatis mi eu libero varius, ac porta sem feugiat. Integer vel pellentesque magna, vel mattis metus. Nulla facilisi. In semper auctor metus, ac maximus leo. Vestibulum pharetra arcu euismod tellus tincidunt venenatis. Curabitur eu libero et dui condimentum malesuada a eu ipsum. Aenean dapibus nulla vel enim iaculis molestie. Maecenas porta tincidunt nibh vitae varius. Fusce sed rutrum nibh, a rutrum diam. Nulla vitae fermentum enim, a dapibus metus. Etiam viverra diam nec imperdiet laoreet.

    Morbi lacus tortor, suscipit eget tellus id, tincidunt porta arcu. Fusce sit amet sollicitudin mi. Sed semper congue luctus. Quisque scelerisque ligula a ornare tristique. Vivamus faucibus augue et vehicula lobortis. Donec ut sollicitudin diam. Donec bibendum arcu ex. Vivamus dictum vestibulum lectus vitae auctor. Vestibulum eget lectus varius, ullamcorper libero vel, consequat elit. Maecenas quis ante in odio pulvinar vehicula. Vestibulum nec enim et enim fermentum bibendum.

    Suspendisse vehicula, sem eu sollicitudin venenatis, justo libero pharetra nisl, quis fringilla nisl sapien at tellus. Sed at dolor tincidunt ex ornare accumsan non ac risus. Etiam feugiat eget tortor nec porta. Nulla gravida nunc eu turpis pretium iaculis. Donec in orci in nisl pharetra consectetur ut quis ligula. Duis lorem felis, tincidunt porttitor nisi a, gravida porttitor justo. Morbi eu rhoncus dolor. Phasellus semper ex ac eros maximus, et elementum quam elementum. Curabitur accumsan sed risus vel semper. Suspendisse pharetra, est eu semper convallis, odio velit imperdiet libero, non molestie nulla lorem eget eros. Integer ut euismod massa. Integer sit amet enim tempor, dapibus diam at, lacinia sem. Integer blandit lorem at blandit aliquam. Aliquam semper lorem ac efficitur cursus.

    """


@pytest.fixture
def encoded_content(text_file_content) -> bytes:
    return text_file_content.encode("utf-8")
