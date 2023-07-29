package com.example.spring.encoder

import org.junit.jupiter.api.Test

class EncoderTest {
    @Test
    fun main() {
        val djangoPbkdf2PasswordEncoder = DjangoPbkdf2PasswordEncoder()
        val password = djangoPbkdf2PasswordEncoder.encode("password")
        System.out.println(password)
        System.out.println(djangoPbkdf2PasswordEncoder.matches("password", password))
    }
}