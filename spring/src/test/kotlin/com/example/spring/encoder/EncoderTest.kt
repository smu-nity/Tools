package com.example.spring.encoder

import org.junit.jupiter.api.Test

class EncoderTest {
    @Test
    fun main() {
        val djangoPbkdf2PasswordEncoder = DjangoPbkdf2PasswordEncoder()
        val password = djangoPbkdf2PasswordEncoder.encode("testtest")
        val encoding = "pbkdf2_sha256\$390000\$8ZcmAeOFPm4ZY2aLYghxzI\$ufspbGraVRYQIv+TrdJDH5jj2V3aMbz+wXx3qgJ8gbE="
        System.out.println(djangoPbkdf2PasswordEncoder.matches("testtest", password))
        System.out.println(djangoPbkdf2PasswordEncoder.matches("testtest", encoding))
    }
}